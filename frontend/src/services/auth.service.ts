import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { Observable, of } from 'rxjs';

import { JwtHelperService } from '@auth0/angular-jwt';
import * as Cookies from 'js-cookie';

import { AccessToken } from '../interfaces/access-token';
import { BasicAuth } from '../interfaces/basic-auth';
import { UrlService } from './url.service';
import {Router} from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  loginPath = '/api/login';
  logoutPath = '/api/logout';

  private token: AccessToken;

  constructor(
    private router: Router,
    private httpClient: HttpClient,
    private urlService: UrlService
  ) { }

  getXAccessTokenHeader(): AccessToken {
    return this.token;
  }

  private loginAPICall(auth: BasicAuth): Observable<any> {
    return this.httpClient.get(this.urlService.getBackendUrl() + this.loginPath, {
      headers: {
        Authorization: 'Basic ' + btoa(auth.username + ':' + auth.password)
      }
    });
  }

  login(auth?: BasicAuth): Observable<any> {
    const localToken = Cookies.get('ipm-token');
    if (localToken) {
      const jwtHelper = new JwtHelperService();
      const decodedToken = jwtHelper.decodeToken(localToken);

      if ((decodedToken.exp * 1000) > Date.now()) {
        this.token = {
          'x-access-token': localToken
        };

        return of({
          ok: this.token !== null,
          token: this.token,
          fromLocal: true
        });
      }
    }

    if (auth) {
      if (auth.client) {
        this.urlService.setClient(auth.client);
      }

      return this.loginAPICall(auth).pipe(
        map(data => {
          if ('token' in data) {
            this.token = {
              'x-access-token': data.token
            };

            // Set token that lasts half a day
            Cookies.set('ipm-token', data.token, { expires: 0.5 });
          }

          return {
            ok: this.token !== null,
            token: this.token,
            fromLocal: false
          };
        })
      );
    }

    return of({
      ok: false,
      token: null,
      fromLocal: false
    });
  }

  logout(): Observable<any> {
    return this.httpClient.get(this.urlService.getBackendUrl() + this.logoutPath, {
      headers: this.getXAccessTokenHeader()
    }).pipe(map(() => {
      Cookies.remove('ipm-token', { path: '' });
    }));
  }
}

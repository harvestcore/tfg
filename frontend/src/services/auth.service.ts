import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { Observable, of } from 'rxjs';

import { JwtHelperService } from '@auth0/angular-jwt';
import * as Cookies from 'js-cookie';

import { AccessToken } from '../interfaces/access-token';
import { BasicAuth } from '../interfaces/basic-auth';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  loginPath = '/api/login';
  logoutPath = '/api/login';

  private token: AccessToken;
  private urlToRedirect: string;

  constructor(
    private httpClient: HttpClient
  ) { }

  setUrlToRedirect(url: string) {
    this.urlToRedirect = url;
  }

  getUrlToRedirect() {
    return this.urlToRedirect;
  }

  getXAccessTokenHeader(): any {
    return {
      ...this.token
    };
  }

  private loginAPICall(auth: BasicAuth): Observable<any> {
    return this.httpClient.get(environment.backendUrl + this.loginPath, {
      headers: {
        Authorization: 'Basic ' + btoa(auth.username + ':' + auth.password)
      }
    });
  }

  login(auth?: BasicAuth): any {
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
      return this.loginAPICall(auth).pipe(
        map(data => {
          if ('token' in data) {
            this.token = {
              'x-access-token': data.token
            };
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
    return this.httpClient.get(environment.backendUrl + this.logoutPath, {
      headers: this.getXAccessTokenHeader()
    });
  }

  getToken(): AccessToken {
    return this.token;
  }
}

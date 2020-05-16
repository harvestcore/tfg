import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';

import { AccessToken } from '../interfaces/access-token';
import { BasicAuth } from '../interfaces/basic-auth';
import { environment } from '../environments/environment';
import { JwtHelperService } from '@auth0/angular-jwt';

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

  login(auth: BasicAuth): any {
    const localToken = localStorage.getItem('ipm-token');
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


    return this.loginAPICall(auth).pipe(
      map(data => {
        if ('token' in data) {
          this.token = {
            'x-access-token': data.token
          };
          localStorage.setItem('ipm-token', data.token);
        }

        return {
          ok: this.token !== null,
          token: this.token
        };
      })
    );
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

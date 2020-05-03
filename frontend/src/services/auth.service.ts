import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

import {BasicAuth} from '../interfaces/basic-auth';
import {environment} from '../environments/environment';
import {AccessToken} from '../interfaces/access-token';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  loginPath = '/api/login';
  logoutPath = '/api/login';
  token: AccessToken;

  constructor(
    private httpClient: HttpClient
  ) { }

  getXAccessTokenHeader(): any {
    return {
      ...this.token
    };
  }

  private loginAPICall(auth: BasicAuth): Observable<any> {
    return this.httpClient.get(environment.backendUrl + this.loginPath, {
      headers: {
        Authorization: 'Basic ' + auth.username + ':' + auth.password
      }
    });
  }

  login(auth: BasicAuth): any {
    this.loginAPICall(auth).subscribe(data => {
      if ('token' in data) {
        this.token = {
          'x-access-token': data.token
        };

        return this.token;
      }

      return false;
    });
  }

  logout(): Observable<any> {
    return this.httpClient.get(environment.backendUrl + this.logoutPath, {
      headers: this.getXAccessTokenHeader()
    });
  }
}

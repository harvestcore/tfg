import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

import {BasicAuth} from '../interfaces/basic-auth';
import {environment} from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  loginPath = '/api/login';
  logoutPath = '/api/login';
  token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiJiM2NmM2E2MS1iNTdiLTQ4MzctODY4Ni1jY2M3YTBjYzMzN2YiLCJleHAiOiIyMDAzMDUyMDE3NDMwNTg0MjIifQ.jAu6m4KLeuEu4F7zSDKOd6UfOwf4krCkSuqjLLeihIk';

  constructor(
    private httpClient: HttpClient
  ) { }

  getXAccessTokenHeader(): any {
    return {
      'x-access-token': this.token
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
        this.token = data.token;
        return {
          'x-access-token': this.token
        };
      }

      return false;
    });
  }

  logout() {
    this.httpClient.get(environment.backendUrl + this.logoutPath, {
      headers: this.getXAccessTokenHeader()
    });
  }
}

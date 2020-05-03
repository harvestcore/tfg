import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';
import {environment} from '../environments/environment';
import {User} from '../interfaces/user';
import {Query} from '../interfaces/query';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  path = '/api/user';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService
  ) { }

  updateUser(email: string, userData: User): Observable<any> {
    return this.httpClient.put(environment.backendUrl + this.path, {
        email,
        data: userData
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  removeUser(email: string): Observable<any> {
    const url = environment.backendUrl + this.path;
    return this.httpClient.request('delete', url, {
        body: {
          email
        },
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  getUser(username: string): Observable<any> {
    const url = environment.backendUrl + this.path + '/' + username;
    return this.httpClient.get(url, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  queryUser(query: Query): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path + '/query', {
        ...query
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  addUser(user: User): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path, {
        ...user
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {catchError, map} from 'rxjs/operators';

import {AuthService} from './auth.service';

import {User} from '../interfaces/user';
import {Query} from '../interfaces/query';
import {UrlService} from './url.service';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private path = '/api/user';

  private currentUser: User;

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService,
    private urlService: UrlService
  ) { }

  setCurrentUser(username: string) {
    return this.getUser(username).pipe(map(user => {
      this.currentUser = user;
    }));
  }

  clearCurrentUser() {
    this.currentUser = null;
  }

  getCurrentUser(): User {
    return this.currentUser;
  }

  userLoggedIn(): boolean {
    return !!this.currentUser;
  }

  updateUser(email: string, userData: User): Observable<any> {
    return this.httpClient.put(this.urlService.getBackendUrl() + this.path, {
        email,
        data: userData
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    ).pipe(
      map(data => {
        return {
          ok: true,
          data
        };
      }),
      catchError(error => {
        return of({
          ok: false,
          error
        });
      })
    );
  }

  removeUser(email: string): Observable<any> {
    const url = this.urlService.getBackendUrl() + this.path;
    return this.httpClient.request('delete', url, {
        body: {
          email
        },
        headers: this.authService.getXAccessTokenHeader()
      }
    ).pipe(
      map(data => {
        return {
          ok: true,
          data
        };
      }),
      catchError(error => {
        return of({
          ok: false,
          error
        });
      })
    );
  }

  getUser(username: string): Observable<any> {
    const url = this.urlService.getBackendUrl() + this.path + '/' + username;
    return this.httpClient.get(url, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  queryUser(query: Query): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path + '/query', {
        ...query
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    ).pipe(
      map(data => {
        return {
          ok: true,
          data
        };
      }),
      catchError(error => {
        return of({
          ok: false,
          error
        });
      })
    );
  }

  addUser(user: User): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path, {
        ...user
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    ).pipe(
      map(data => {
        return {
          ok: true,
          data
        };
      }),
      catchError(error => {
        return of({
          ok: false,
          error
        });
      })
    );
  }
}

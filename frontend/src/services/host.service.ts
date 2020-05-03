import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';
import {environment} from '../environments/environment';
import {Host} from '../interfaces/host';
import {Query} from '../interfaces/query';

@Injectable({
  providedIn: 'root'
})
export class HostService {
  path = '/api/provision/host';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService
  ) { }

  updateHost(name: string, hostData: Host): Observable<any> {
    return this.httpClient.put(environment.backendUrl + this.path, {
        name,
        data: hostData
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  removeHost(name: string): Observable<any> {
    const url = environment.backendUrl + this.path;
    return this.httpClient.request('delete', url, {
        body: {
          name
        },
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  getHost(name: string): Observable<any> {
    const url = environment.backendUrl + this.path + '/' + name;
    return this.httpClient.get(url, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  queryHost(query: Query): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path + '/query', {
        ...query
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  addHost(host: Host): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path, {
        ...host
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';

import {Host} from '../interfaces/host';
import {Query} from '../interfaces/query';
import {UrlService} from './url.service';

@Injectable({
  providedIn: 'root'
})
export class HostService {
  path = '/api/provision/host';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService,
    private urlService: UrlService
  ) { }

  updateHost(name: string, hostData: Host): Observable<any> {
    return this.httpClient.put(this.urlService.getBackendUrl() + this.path, {
        name,
        data: hostData
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  removeHost(name: string): Observable<any> {
    const url = this.urlService.getBackendUrl() + this.path;
    return this.httpClient.request('delete', url, {
        body: {
          name
        },
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  getHost(name: string): Observable<any> {
    const url = this.urlService.getBackendUrl() + this.path + '/' + name;
    return this.httpClient.get(url, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  queryHost(query: Query): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path + '/query', {
        ...query
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  addHost(host: Host): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path, {
        ...host
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';

import {Machine} from '../interfaces/machine';
import {Query} from '../interfaces/query';
import {UrlService} from './url.service';

@Injectable({
  providedIn: 'root'
})
export class MachineService {
  path = '/api/machine';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService,
    private urlService: UrlService
  ) { }

  updateMachine(name: string, machineData: Machine): Observable<any> {
    return this.httpClient.put(this.urlService.getBackendUrl() + this.path, {
        name,
        data: machineData
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  removeMachine(name: string): Observable<any> {
    const url = this.urlService.getBackendUrl() + this.path;
    return this.httpClient.request('delete', url, {
        body: {
          name
        },
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  getMachine(name: string): Observable<any> {
    const url = this.urlService.getBackendUrl() + this.path + '/' + name;
    return this.httpClient.get(url, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  queryMachine(query: Query): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path + '/query', {
        ...query
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  addMachine(machine: Machine): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path, {
        ...machine
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';
import {environment} from '../environments/environment';
import {Machine} from '../interfaces/machine';
import {Query} from '../interfaces/query';

@Injectable({
  providedIn: 'root'
})
export class MachineService {
  path = '/api/machine';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService
  ) { }

  updateMachine(name: string, machineData: Machine): Observable<any> {
    return this.httpClient.put(environment.backendUrl + this.path, {
        name,
        data: machineData
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  removeMachine(name: string): Observable<any> {
    const url = environment.backendUrl + this.path;
    return this.httpClient.request('delete', url, {
        body: {
          name
        },
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  getMachine(name: string): Observable<any> {
    const url = environment.backendUrl + this.path + '/' + name;
    return this.httpClient.get(url, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  queryMachine(query: Query): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path + '/query', {
        ...query
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  addMachine(machine: Machine): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path, {
        ...machine
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

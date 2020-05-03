import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';
import {environment} from '../environments/environment';
import {Playbook} from '../interfaces/playbook';
import {Query} from '../interfaces/query';

@Injectable({
  providedIn: 'root'
})
export class PlaybookService {
  path = '/api/provision/host';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService
  ) { }

  updatePlaybook(name: string, hostPlaybook: Playbook): Observable<any> {
    return this.httpClient.put(environment.backendUrl + this.path, {
        name,
        data: hostPlaybook
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  removePlaybook(name: string): Observable<any> {
    const url = environment.backendUrl + this.path;
    return this.httpClient.request('delete', url, {
        body: {
          name
        },
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  getPlaybook(name: string): Observable<any> {
    const url = environment.backendUrl + this.path + '/' + name;
    return this.httpClient.get(url, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  queryPlaybook(query: Query): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path + '/query', {
        ...query
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  addPlaybook(playbook: Playbook): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path, {
        ...playbook
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

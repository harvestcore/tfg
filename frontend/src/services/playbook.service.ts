import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';

import {Playbook} from '../interfaces/playbook';
import {Query} from '../interfaces/query';
import {UrlService} from './url.service';

@Injectable({
  providedIn: 'root'
})
export class PlaybookService {
  path = '/api/provision/host';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService,
    private urlService: UrlService
  ) { }

  updatePlaybook(name: string, hostPlaybook: Playbook): Observable<any> {
    return this.httpClient.put(this.urlService.getBackendUrl() + this.path, {
        name,
        data: hostPlaybook
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  removePlaybook(name: string): Observable<any> {
    const url = this.urlService.getBackendUrl() + this.path;
    return this.httpClient.request('delete', url, {
        body: {
          name
        },
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  getPlaybook(name: string): Observable<any> {
    const url = this.urlService.getBackendUrl() + this.path + '/' + name;
    return this.httpClient.get(url, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  queryPlaybook(query: Query): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path + '/query', {
        ...query
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  addPlaybook(playbook: Playbook): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path, {
        ...playbook
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

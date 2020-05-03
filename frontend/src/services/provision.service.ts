import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';
import {environment} from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProvisionService {
  path = '/api/provision';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService
  ) { }

  runPlaybook(hosts: [string], playbook: string, passwords: any): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path, {
        hosts,
        playbook,
        passwords
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

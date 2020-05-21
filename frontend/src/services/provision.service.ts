import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';

import {AuthService} from './auth.service';

import {UrlService} from './url.service';
import {catchError, map} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ProvisionService {
  path = '/api/provision';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService,
    private urlService: UrlService
  ) { }

  runPlaybook(hosts: [string], playbook: string, passwords: any): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path, {
        hosts,
        playbook,
        passwords
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

import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';
import {UrlService} from './url.service';

@Injectable({
  providedIn: 'root'
})
export class StatusService {

  path = '/api/status';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService,
    private urlService: UrlService
  ) {}

  getStatus(): Observable<any> {
    return this.httpClient.get(
      this.urlService.getBackendUrl() + this.path,
      {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

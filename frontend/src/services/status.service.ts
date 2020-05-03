import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class StatusService {

  path = '/api/status';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService
  ) {}

  getStatus(): Observable<any> {
    return this.httpClient.get(
      environment.backendUrl + this.path,
      {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

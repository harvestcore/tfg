import {HttpClient, HttpHeaders} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';
import {Observable} from 'rxjs';
import {StatusResponse} from '../interfaces/status';
import {AuthService} from './auth.service';

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

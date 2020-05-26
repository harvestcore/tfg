import {HttpClient} from '@angular/common/http';
import {EventEmitter, Injectable} from '@angular/core';
import {interval, Observable, of} from 'rxjs';

import {AuthService} from './auth.service';
import {UrlService} from './url.service';
import {catchError, flatMap, map} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class StatusService {
  heartbeatInterval = 10000;
  notifier = new EventEmitter();
  path = '/api/status';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService,
    private urlService: UrlService
  ) {
    interval(this.heartbeatInterval).pipe(
      flatMap(() => this.getStatus())
    ).subscribe(response => {
      this.getStatus().subscribe(hbResponse => {
        this.notifier.emit({
          online: true,
          ...hbResponse
        });
      });
    },
    error => {
      this.notifier.emit({
        online: false,
        error
      });
    });
  }

  getStatus(): Observable<any> {
    return this.httpClient.get(
      this.urlService.getBackendUrl() + this.path,
      {
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

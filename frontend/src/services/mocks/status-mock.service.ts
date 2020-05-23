import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class StatusMockService {
  constructor() {}

  getStatus(): Observable<any> {
    return of({});
  }
}

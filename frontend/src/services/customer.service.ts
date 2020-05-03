import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';
import {Customer} from '../interfaces/customer';
import {environment} from '../environments/environment';
import {Query} from '../interfaces/query';

@Injectable({
  providedIn: 'root'
})
export class CustomerService {

  path = '/api/customer';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService
  ) { }

  updateCustomer(domain: string, customerData: Customer): Observable<any> {
    return this.httpClient.put(environment.backendUrl + this.path, {
      domain,
      data: customerData
    }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  removeCustomer(domain: string): Observable<any> {
    const url = environment.backendUrl + this.path;
    return this.httpClient.request('delete', url, {
        body: {
          domain
        },
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  queryCustomer(query: Query): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path + '/query', {
        ...query
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  addCustomer(customer: Customer): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path, {
        domain: customer.domain,
        db_name: customer.db_name
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';
import {Customer} from '../interfaces/customer';

import {Query} from '../interfaces/query';
import {UrlService} from './url.service';

@Injectable({
  providedIn: 'root'
})
export class CustomerService {

  path = '/api/customer';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService,
    private urlService: UrlService
  ) { }

  updateCustomer(domain: string, customerData: Customer): Observable<any> {
    return this.httpClient.put(this.urlService.getBackendUrl() + this.path, {
      domain,
      data: customerData
    }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  removeCustomer(domain: string): Observable<any> {
    const url = this.urlService.getBackendUrl() + this.path;
    return this.httpClient.request('delete', url, {
        body: {
          domain
        },
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  queryCustomer(query: Query): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path + '/query', {
        ...query
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  addCustomer(customer: Customer): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path, {
        domain: customer.domain,
        db_name: customer.db_name
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

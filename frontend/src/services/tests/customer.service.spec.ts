import {HttpClientTestingModule} from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';

import { CustomerService } from '../customer.service';
import {AuthService} from '../auth.service';

describe('CustomerService', () => {
  let service: CustomerService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [AuthService, CustomerService]
    });
    service = TestBed.inject(CustomerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

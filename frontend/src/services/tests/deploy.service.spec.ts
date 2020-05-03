import { TestBed } from '@angular/core/testing';

import { DeployService } from '../deploy.service';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import {AuthService} from '../auth.service';
import {CustomerService} from '../customer.service';

describe('DeployService', () => {
  let service: DeployService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [AuthService, DeployService]
    });
    service = TestBed.inject(DeployService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

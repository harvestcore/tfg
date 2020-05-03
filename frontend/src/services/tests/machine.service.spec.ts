import { TestBed } from '@angular/core/testing';

import { MachineService } from '../machine.service';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import {AuthService} from '../auth.service';
import {CustomerService} from '../customer.service';

describe('MachineService', () => {
  let service: MachineService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [AuthService, MachineService]
    });
    service = TestBed.inject(MachineService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

import { TestBed } from '@angular/core/testing';

import { ProvisionService } from '../provision.service';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import {AuthService} from '../auth.service';
import {MachineService} from '../machine.service';

describe('ProvisionService', () => {
  let service: ProvisionService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [AuthService, ProvisionService]
    });
    service = TestBed.inject(ProvisionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

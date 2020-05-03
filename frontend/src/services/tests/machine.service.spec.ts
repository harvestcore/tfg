import { TestBed } from '@angular/core/testing';

import {AuthService} from '../auth.service';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import { MachineService } from '../machine.service';

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

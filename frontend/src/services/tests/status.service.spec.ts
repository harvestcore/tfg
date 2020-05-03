import { TestBed } from '@angular/core/testing';

import { StatusService } from '../status.service';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import {AuthService} from '../auth.service';
import {MachineService} from '../machine.service';

describe('StatusService', () => {
  let service: StatusService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [AuthService, StatusService]
    });
    service = TestBed.inject(StatusService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

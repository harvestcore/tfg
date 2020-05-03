import { TestBed } from '@angular/core/testing';

import { UserService } from '../user.service';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import {AuthService} from '../auth.service';
import {MachineService} from '../machine.service';

describe('UserService', () => {
  let service: UserService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [AuthService, UserService]
    });
    service = TestBed.inject(UserService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

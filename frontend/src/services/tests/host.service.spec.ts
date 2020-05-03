import {HttpClientTestingModule} from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';

import { HostService } from '../host.service';
import {AuthService} from '../auth.service';

describe('HostService', () => {
  let service: HostService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [AuthService, HostService]
    });
    service = TestBed.inject(HostService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

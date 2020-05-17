import { TestBed } from '@angular/core/testing';

import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';

import { AuthService } from '../auth.service';
import { ProvisionService } from '../provision.service';
import { UrlService } from '../url.service';

describe('ProvisionService', () => {
  let service: ProvisionService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, RouterTestingModule],
      providers: [AuthService, ProvisionService, UrlService]
    });
    service = TestBed.inject(ProvisionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

import { TestBed } from '@angular/core/testing';

import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';

import { AuthService } from '../auth.service';
import { DeployService } from '../deploy.service';
import { UrlService } from '../url.service';

describe('DeployService', () => {
  let service: DeployService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, RouterTestingModule],
      providers: [AuthService, DeployService, UrlService]
    });
    service = TestBed.inject(DeployService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

import { TestBed } from '@angular/core/testing';

import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';

import { AuthService } from '../auth.service';
import { PlaybookService } from '../playbook.service';
import { UrlService } from '../url.service';

describe('PlaybookService', () => {
  let service: PlaybookService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, RouterTestingModule],
      providers: [AuthService, PlaybookService, UrlService]
    });
    service = TestBed.inject(PlaybookService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

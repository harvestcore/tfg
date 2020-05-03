import { TestBed } from '@angular/core/testing';

import {AuthService} from '../auth.service';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import { PlaybookService } from '../playbook.service';

describe('PlaybookService', () => {
  let service: PlaybookService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [AuthService, PlaybookService]
    });
    service = TestBed.inject(PlaybookService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

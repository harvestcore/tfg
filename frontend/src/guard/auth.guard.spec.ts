import { TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';

import { AuthGuard } from './auth.guard';
import { UserService } from '../services/user.service';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import {CUSTOM_ELEMENTS_SCHEMA} from '@angular/core';
import {StatusService} from '../services/status.service';
import {AuthService} from '../services/auth.service';
import {UserMockService} from '../services/mocks/user-mock.service';
import {StatusMockService} from '../services/mocks/status-mock.service';
import {AuthMockService} from '../services/mocks/auth-mock.service';

describe('AuthGuard', () => {
  let guard: AuthGuard;
  const mockUserService = new UserMockService();
  const mockStatusService = new StatusMockService();
  const mockAuthService = new AuthMockService();

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, RouterTestingModule],
      providers: [
        { provide: UserService, useValue: mockUserService },
        { provide: StatusService, useValue: mockStatusService },
        { provide: AuthService, useValue: mockAuthService }
      ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA]
    });
    guard = TestBed.inject(AuthGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});

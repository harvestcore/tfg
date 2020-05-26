import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

import { imports } from '../app.module.js';
import { TopNavigatorComponent } from './top-navigator.component';
import {UserService} from '../../services/user.service';
import {AuthService} from '../../services/auth.service';
import {AuthMockService} from '../../services/mocks/auth-mock.service';
import {UserMockService} from '../../services/mocks/user-mock.service';

describe('TopNavigatorComponent', () => {
  let component: TopNavigatorComponent;
  let fixture: ComponentFixture<TopNavigatorComponent>;
  const mockAuthService = new AuthMockService();
  const mockUserService = new UserMockService();

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports,
      providers: [
        { provide: UserService, useValue: mockUserService },
        { provide: AuthService, useValue: mockAuthService }
      ],
      declarations: [ TopNavigatorComponent ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TopNavigatorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

import { imports } from '../app.module.js';
import { TopNavigatorComponent } from './top-navigator.component';

describe('TopNavigatorComponent', () => {
  let component: TopNavigatorComponent;
  let fixture: ComponentFixture<TopNavigatorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports,
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

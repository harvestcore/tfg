import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AreyousuredialogComponent } from './areyousuredialog.component';
import { imports } from '../app.module.js';
import {MAT_DIALOG_DATA} from '@angular/material/dialog';
import {CUSTOM_ELEMENTS_SCHEMA} from '@angular/core';

describe('AreyousuredialogComponent', () => {
  let component: AreyousuredialogComponent;
  let fixture: ComponentFixture<AreyousuredialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports,
      declarations: [ AreyousuredialogComponent ],
      providers: [
        {
          provide: MAT_DIALOG_DATA,
          useValue: {}
        }
      ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AreyousuredialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

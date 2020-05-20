import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MachinesdialogComponent } from './machinesdialog.component';
import { imports } from '../../app.module.js';
import {MAT_DIALOG_DATA} from '@angular/material/dialog';

describe('MachinesdialogComponent', () => {
  let component: MachinesdialogComponent;
  let fixture: ComponentFixture<MachinesdialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports,
      declarations: [ MachinesdialogComponent ],
      providers: [
        {
          provide: MAT_DIALOG_DATA,
          useValue: {}
        }
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MachinesdialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

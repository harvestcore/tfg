import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MachinesComponent } from './machines.component';
import { imports } from '../app.module.js';
import {CUSTOM_ELEMENTS_SCHEMA} from '@angular/core';
import {MachineService} from '../../services/machine.service';
import {MachineMockService} from '../../services/mocks/machine-mock.service';

describe('MachinesComponent', () => {
  let component: MachinesComponent;
  let fixture: ComponentFixture<MachinesComponent>;
  const machineMockService = new MachineMockService();

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports,
      providers: [ { provide: MachineService, useValue: machineMockService } ],
      declarations: [ MachinesComponent ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MachinesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

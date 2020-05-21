import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RunplaybookdialogComponent } from './runplaybookdialog.component';

describe('RunplaybookdialogComponent', () => {
  let component: RunplaybookdialogComponent;
  let fixture: ComponentFixture<RunplaybookdialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RunplaybookdialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RunplaybookdialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

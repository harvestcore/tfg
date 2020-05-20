import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MachinesdialogComponent } from './machinesdialog.component';

describe('MachinesdialogComponent', () => {
  let component: MachinesdialogComponent;
  let fixture: ComponentFixture<MachinesdialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MachinesdialogComponent ]
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

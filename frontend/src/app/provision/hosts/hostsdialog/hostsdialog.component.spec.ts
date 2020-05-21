import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HostsdialogComponent } from './hostsdialog.component';

describe('HostsdialogComponent', () => {
  let component: HostsdialogComponent;
  let fixture: ComponentFixture<HostsdialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HostsdialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HostsdialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

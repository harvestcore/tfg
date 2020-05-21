import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PlaybooksdialogComponent } from './playbooksdialog.component';

describe('PlaybooksdialogComponent', () => {
  let component: PlaybooksdialogComponent;
  let fixture: ComponentFixture<PlaybooksdialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PlaybooksdialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PlaybooksdialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

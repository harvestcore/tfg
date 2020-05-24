import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListImageDialogComponent } from './list-image-dialog.component';

describe('ListImageDialogComponent', () => {
  let component: ListImageDialogComponent;
  let fixture: ComponentFixture<ListImageDialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListImageDialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListImageDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

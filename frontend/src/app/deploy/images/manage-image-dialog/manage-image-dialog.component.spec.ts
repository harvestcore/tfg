import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ManageImageDialogComponent } from './manage-image-dialog.component';

describe('ManageImageDialogComponent', () => {
  let component: ManageImageDialogComponent;
  let fixture: ComponentFixture<ManageImageDialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ManageImageDialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ManageImageDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

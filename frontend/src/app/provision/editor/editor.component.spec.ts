import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EditorComponent } from './editor.component';
import { imports} from '../../app.module';
import { HostService } from '../../../services/host.service';
import { HostMockService } from '../../../services/mocks/host-mock.service';
import { PlaybookService } from '../../../services/playbook.service';
import { PlaybookMockService } from '../../../services/mocks/playbook-mock.service';

describe('EditorComponent', () => {
  let component: EditorComponent;
  let fixture: ComponentFixture<EditorComponent>;
  const hostMockService = new HostMockService();
  const playbookMockService = new PlaybookMockService();

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports,
      providers: [
        { provide: HostService, useValue: hostMockService },
        { provide: PlaybookService, useValue: playbookMockService }
      ],
      declarations: [ EditorComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EditorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

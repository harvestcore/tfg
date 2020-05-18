import { NgModule } from '@angular/core';

import { FontAwesomeModule, FaIconLibrary } from '@fortawesome/angular-fontawesome';
import {
  faLaptop,
  faCogs,
  faHdd,
  faServer,
  faChartPie,
  faUserShield,
  faUser,
  faHeartBroken,
  faChevronDown,
  faFrown,
  faExclamationTriangle,
  faTimes,
  faEye,
  faEdit,
  faTrash
} from '@fortawesome/free-solid-svg-icons';

import { faDocker } from '@fortawesome/free-brands-svg-icons';

const icons = [
  faDocker,
  faLaptop,
  faCogs,
  faHdd,
  faServer,
  faChartPie,
  faUserShield,
  faUser,
  faChevronDown,
  faHeartBroken,
  faFrown,
  faExclamationTriangle,
  faTimes,
  faEye,
  faEdit,
  faTrash
];

@NgModule({
  imports: [FontAwesomeModule],
  exports: [FontAwesomeModule],
})
export class FontAwesomeIconsModule {
  constructor(library: FaIconLibrary) {
    library.addIcons(...icons);
  }
}

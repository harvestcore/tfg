import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { FlexLayoutModule } from '@angular/flex-layout';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule } from '@angular/material/button';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatCardModule } from '@angular/material/card';
import { MatMenuModule } from '@angular/material/menu';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatToolbarModule } from '@angular/material/toolbar';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { AuthService } from '../services/auth.service';
import { CustomerService } from '../services/customer.service';
import { DeployService } from '../services/deploy.service';
import { HostService } from '../services/host.service';
import { MachineService } from '../services/machine.service';
import { PlaybookService } from '../services/playbook.service';
import { ProvisionService } from '../services/provision.service';
import { StatusService } from '../services/status.service';
import { UserService } from '../services/user.service';

import { MainContainerComponent } from './main-container/main-container.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { TopNavigatorComponent } from './top-navigator/top-navigator.component';

import { FontAwesomeModule, FaIconLibrary } from '@fortawesome/angular-fontawesome';
import { faLaptop, faCogs, faHdd, faServer, faChartPie, faUserShield, faUser, faChevronDown } from '@fortawesome/free-solid-svg-icons';
import { faDocker } from '@fortawesome/free-brands-svg-icons';
import {MatGridListModule} from '@angular/material/grid-list';

const providers = [
  AuthService,
  CustomerService,
  DeployService,
  HostService,
  MachineService,
  PlaybookService,
  ProvisionService,
  StatusService,
  UserService
];

const imports = [
  AppRoutingModule,
  BrowserAnimationsModule,
  BrowserModule,
  FlexLayoutModule,
  FontAwesomeModule,
  HttpClientModule,
  MatMenuModule,
  MatToolbarModule
];

@NgModule({
  declarations: [
    AppComponent,
    NotFoundComponent,
    TopNavigatorComponent,
    MainContainerComponent
  ],
  imports: [
    imports,
    MatSlideToggleModule,
    MatButtonToggleModule,
    MatButtonModule,
    MatMenuModule,
    MatCardModule,
    MatGridListModule
  ],
  providers,
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor(private iconLibrary: FaIconLibrary) {
    iconLibrary.addIcons(
      faDocker,
      faLaptop,
      faCogs,
      faHdd,
      faServer,
      faChartPie,
      faUserShield,
      faUser,
      faChevronDown
    );
  }
}

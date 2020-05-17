import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { FlexLayoutModule } from '@angular/flex-layout';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule } from '@angular/material/button';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatCardModule} from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatInputModule } from '@angular/material/input';
import { MatMenuModule } from '@angular/material/menu';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatToolbarModule } from '@angular/material/toolbar';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { AuthService } from '../services/auth.service';
import { CustomerService } from '../services/customer.service';
import { DeployService } from '../services/deploy.service';
import { HostService } from '../services/host.service';
import { MachineService } from '../services/machine.service';
import { PlaybookService } from '../services/playbook.service';
import { ProvisionService } from '../services/provision.service';
import { StatusService } from '../services/status.service';
import { UrlService } from '../services/url.service';
import { UserService } from '../services/user.service';


import { MainContainerComponent } from './main-container/main-container.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { TopNavigatorComponent } from './top-navigator/top-navigator.component';
import { FontAwesomeIconsModule } from '../icons/FontAwesomeIconsModule';
import { LoginComponent } from './login/login.component';

const providers = [
  AuthService,
  CustomerService,
  DeployService,
  HostService,
  MachineService,
  PlaybookService,
  ProvisionService,
  StatusService,
  UrlService,
  UserService
];

export const imports = [
  AppRoutingModule,
  BrowserAnimationsModule,
  BrowserModule,
  FlexLayoutModule,
  FontAwesomeIconsModule,
  HttpClientModule,
  MatButtonModule,
  MatButtonToggleModule,
  MatCardModule,
  MatFormFieldModule,
  MatGridListModule,
  MatInputModule,
  MatMenuModule,
  MatSlideToggleModule,
  MatToolbarModule,
  ReactiveFormsModule
];

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    NotFoundComponent,
    MainContainerComponent,
    TopNavigatorComponent,
  ],
    imports: [
        imports
    ],
  providers,
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor() {
  }
}

import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import {AuthService} from '../services/auth.service';
import {CustomerService} from '../services/customer.service';
import {DeployService} from '../services/deploy.service';
import {HostService} from '../services/host.service';
import {MachineService} from '../services/machine.service';
import {PlaybookService} from '../services/playbook.service';
import {ProvisionService} from '../services/provision.service';
import {StatusService} from '../services/status.service';
import {UserService} from '../services/user.service';
import { NotFoundComponent } from './not-found/not-found.component';

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

@NgModule({
  declarations: [
    AppComponent,
    NotFoundComponent
  ],
  imports: [
    AppRoutingModule,
    BrowserModule,
    HttpClientModule
  ],
  providers,
  bootstrap: [AppComponent]
})
export class AppModule { }

import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { FlexLayoutModule } from '@angular/flex-layout';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule } from '@angular/material/button';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatCardModule} from '@angular/material/card';
import { MatDialogModule } from '@angular/material/dialog';
import { MatDividerModule } from '@angular/material/divider';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatInputModule } from '@angular/material/input';
import { MatMenuModule } from '@angular/material/menu';
import { MatPaginatorModule} from '@angular/material/paginator';
import { MatSelectModule } from '@angular/material/select';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatSortModule } from '@angular/material/sort';
import { MatTableModule} from '@angular/material/table';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTooltipModule } from '@angular/material/tooltip';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { FontAwesomeIconsModule } from '../icons/FontAwesomeIconsModule';

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

import { IpmtableComponent } from './ipmtable/ipmtable.component';
import { LoginComponent } from './login/login.component';
import { MachinesComponent } from './machines/machines.component';
import { MainContainerComponent } from './main-container/main-container.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { TopNavigatorComponent } from './top-navigator/top-navigator.component';
import { MachinesdialogComponent } from './machines/machinesdialog/machinesdialog.component';
import { AreyousuredialogComponent } from './areyousuredialog/areyousuredialog.component';

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
  FormsModule,
  HttpClientModule,
  MatButtonModule,
  MatButtonToggleModule,
  MatCardModule,
  MatDialogModule,
  MatDividerModule,
  MatFormFieldModule,
  MatGridListModule,
  MatInputModule,
  MatMenuModule,
  MatPaginatorModule,
  MatSelectModule,
  MatSlideToggleModule,
  MatSnackBarModule,
  MatSortModule,
  MatTableModule,
  MatToolbarModule,
  MatTooltipModule,
  ReactiveFormsModule
];

@NgModule({
  declarations: [
    AppComponent,
    IpmtableComponent,
    LoginComponent,
    MachinesComponent,
    MainContainerComponent,
    NotFoundComponent,
    TopNavigatorComponent,
    MachinesdialogComponent,
    AreyousuredialogComponent,
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

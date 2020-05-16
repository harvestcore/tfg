import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AuthGuard } from './guard/auth.guard';

import { LoginComponent } from './login/login.component';
import { MainContainerComponent } from './main-container/main-container.component';
import { NotFoundComponent } from './not-found/not-found.component';

const routes: Routes = [
  { path: '', canActivate: [AuthGuard], component: MainContainerComponent},
  { path: 'login', component: LoginComponent},
  { path: '**', canActivate: [AuthGuard], component: NotFoundComponent} // 404 component
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

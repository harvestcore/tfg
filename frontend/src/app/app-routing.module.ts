import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {NotFoundComponent} from './not-found/not-found.component';
import {MainContainerComponent} from './main-container/main-container.component';

const routes: Routes = [
  { path: '', component: MainContainerComponent},
  { path: '**', component: NotFoundComponent} // 404 component
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

import { Component, Input, OnInit, ViewChild } from '@angular/core';

import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-ipmtable',
  templateUrl: './ipmtable.component.html',
  styleUrls: ['./ipmtable.component.css']
})
export class IpmtableComponent implements OnInit {
  filter: string;
  dataSource: MatTableDataSource<any>;

  @Input() title: string;
  @Input() displayedColumns: string[];
  @Input() data: any;

  @Input() detailCallback: any;
  @Input() editCallback: any;
  @Input() removeCallback: any;

  @ViewChild(MatPaginator, {static: true}) paginator: MatPaginator;
  @ViewChild(MatSort, {static: true}) sort: MatSort;

  constructor() { }

  ngOnInit(): void {
    if (this.detailCallback || this.editCallback || this.removeCallback) {
      this.displayedColumns.push('actions');
    }

    this.dataSource = new MatTableDataSource<any>(this.data);
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  clearFilter() {
    this.filter = '';
    this.applyFilter();
  }

  applyFilter() {
    if (this.filter || this.filter === '') {
      this.dataSource.filter = this.filter.trim().toLowerCase();
      if (this.dataSource.paginator) {
        this.dataSource.paginator.firstPage();
      }
    }
  }

}
